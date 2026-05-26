import { useEffect, useState } from "react"
import {
  ChevronRight,
  ChevronDown,
  File,
  Folder,
  FolderOpen,
} from "lucide-react"

import type { Panel, FileTab } from "../App"

const LANG_COLORS: Record<string, string> = {
  python: "#3b82f6",
  typescript: "#06b6d4",
  javascript: "#f59e0b",
  toml: "#f59e0b",
  cmake: "#a78bfa",
  css: "#38bdf8",
  json: "#10b981",
  rust: "#f97316",
  markdown: "#e2e8f0",
  text: "#64748b",
}

interface TreeNode {
  name: string
  path: string
  type: "file" | "dir"
  children?: TreeNode[]
}

function detectLanguage(name: string): string {
  const ext = name.split(".").pop()?.toLowerCase()

  switch (ext) {
    case "py":
      return "python"

    case "ts":
    case "tsx":
      return "typescript"

    case "js":
    case "jsx":
      return "javascript"

    case "css":
      return "css"

    case "json":
      return "json"

    case "toml":
      return "toml"

    case "rs":
      return "rust"

    case "cpp":
    case "cc":
    case "cxx":
      return "cpp"

    case "cmake":
      return "cmake"

    case "md":
      return "markdown"

    default:
      return "text"
  }
}

function TreeItem({
  node,
  depth,
  onOpen,
}: {
  node: TreeNode
  depth: number
  onOpen: (f: FileTab) => void
}) {
  const [open, setOpen] = useState(depth < 1)

  const isDir = node.type === "dir"

  return (
    <div>
      <div
        className={`tree-item ${!isDir ? "tree-item--file" : ""}`}
        style={{ paddingLeft: `${8 + depth * 12}px` }}
        onClick={() => {
          if (isDir) {
            setOpen((v) => !v)
            return
          }

          onOpen({
            id: node.path,
            name: node.name,
            path: node.path,
            content: "",
            language: detectLanguage(node.name),
            dirty: false,
          })
        }}
      >
        {isDir ? (
          <>
            {open ? (
              <ChevronDown
                size={12}
                strokeWidth={1.8}
                className="tree-chevron"
              />
            ) : (
              <ChevronRight
                size={12}
                strokeWidth={1.8}
                className="tree-chevron"
              />
            )}

            {open ? (
              <FolderOpen
                size={14}
                strokeWidth={1.6}
                style={{
                  color: "#fbbf24",
                  flexShrink: 0,
                }}
              />
            ) : (
              <Folder
                size={14}
                strokeWidth={1.6}
                style={{
                  color: "#fbbf24",
                  flexShrink: 0,
                }}
              />
            )}
          </>
        ) : (
          <File
            size={14}
            strokeWidth={1.6}
            style={{
              color:
                LANG_COLORS[detectLanguage(node.name)] ?? "#64748b",
              flexShrink: 0,
            }}
          />
        )}

        <span className="tree-label">{node.name}</span>
      </div>

      {isDir &&
        open &&
        node.children?.map((child) => (
          <TreeItem
            key={child.path}
            node={child}
            depth={depth + 1}
            onOpen={onOpen}
          />
        ))}
    </div>
  )
}

interface Props {
  panel: Panel
  onOpenFile: (f: FileTab) => void
}

export default function Sidebar({
  panel,
  onOpenFile,
}: Props) {
  const [search, setSearch] = useState("")
  const [tree, setTree] = useState<TreeNode | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch("http://localhost:8000/api/files/tree")
      .then((r) => r.json())
      .then((data) => {
        setTree(data)
        setLoading(false)
      })
      .catch(() => {
        setLoading(false)
      })
  }, [])

  return (
    <div className="sidebar">
      {panel === "explorer" && (
        <>
          <div className="sidebar__header">
            EXPLORER
          </div>

          <div className="sidebar__tree">
            {loading && (
              <div className="sidebar__empty">
                Loading...
              </div>
            )}

            {!loading && tree && (
              <TreeItem
                node={tree}
                depth={0}
                onOpen={onOpenFile}
              />
            )}

            {!loading && !tree && (
              <div className="sidebar__empty">
                Failed to load workspace
              </div>
            )}
          </div>
        </>
      )}

      {panel === "search" && (
        <>
          <div className="sidebar__header">
            SEARCH
          </div>

          <div className="sidebar__search">
            <input
              className="search-input"
              placeholder="Search in files..."
              value={search}
              onChange={(e) =>
                setSearch(e.target.value)
              }
            />

            {search && (
              <div className="search-results">
                <div className="search-result-item">
                  <span className="search-result-file">
                    Search not implemented
                  </span>
                </div>
              </div>
            )}
          </div>
        </>
      )}

      {panel === "git" && (
        <>
          <div className="sidebar__header">
            SOURCE CONTROL
          </div>

          <div className="sidebar__empty">
            No changes
          </div>
        </>
      )}

      {panel === "extensions" && (
        <>
          <div className="sidebar__header">
            EXTENSIONS
          </div>

          <div className="sidebar__empty">
            No extensions installed
          </div>
        </>
      )}
    </div>
  )
}