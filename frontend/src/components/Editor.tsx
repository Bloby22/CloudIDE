import MonacoEditor from "@monaco-editor/react"
import type { FileTab } from "@/App"

interface Props {
  file: FileTab
  onChange: (content: string) => void
}

export default function Editor({ file, onChange }: Props) {
  return (
    <div className="editor">
      <MonacoEditor
        height="100%"
        theme="vs-dark"
        language={file.language}
        value={file.content}
        onChange={(value) => onChange(value ?? "")}
        options={{
          fontSize: 14,
          minimap: { enabled: true },
          smoothScrolling: true,
          automaticLayout: true,
          tabSize: 2,
          padding: {
            top: 16,
          },
          scrollbar: {
            verticalScrollbarSize: 10,
            horizontalScrollbarSize: 10,
          },
        }}
      />
    </div>
  )
}