cmake_minimum_required(VERSION 3.20)
project(CloudIDE VERSION 0.1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG REQUIRED)

include(FetchContent)

FetchContent_Declare(nlohmann_json
    GIT_REPOSITORY https://github.com/nlohmann/json.git
    GIT_TAG v3.11.3)
FetchContent_MakeAvailable(nlohmann_json)

FetchContent_Declare(httplib
    GIT_REPOSITORY https://github.com/yhirose/cpp-httplib.git
    GIT_TAG v0.15.3)
FetchContent_MakeAvailable(httplib)

FetchContent_Declare(reproc
    GIT_REPOSITORY https://github.com/DaanDeMeyer/reproc.git
    GIT_TAG v14.2.4)
FetchContent_MakeAvailable(reproc)

set(INSTALL_ROOT  ${CMAKE_SOURCE_DIR}/dist)
set(INSTALL_BIN   ${INSTALL_ROOT}/bin)
set(INSTALL_BUILD ${INSTALL_ROOT}/build)
set(INSTALL_LIB   ${INSTALL_ROOT}/lib)

add_subdirectory(Bootstrap)
add_subdirectory(Launcher)
add_subdirectory(bin/CLI)
add_subdirectory(bin/LSP)
add_subdirectory(bin/Format)
add_subdirectory(bin/Lint)
add_subdirectory(bin/Build)
add_subdirectory(bin/Debug)
add_subdirectory(build/core/Engine)
add_subdirectory(build/core/Runtime)
add_subdirectory(build/core/Compiler)
add_subdirectory(build/core/Debugger)
add_subdirectory(build/editor/TreeSitter)
add_subdirectory(build/editor/Lexer)
add_subdirectory(build/editor/Formatter)
add_subdirectory(build/editor/Indexer)
add_subdirectory(build/system/Watcher)
add_subdirectory(build/system/Reproc)
add_subdirectory(build/system/Terminal)
add_subdirectory(build/system/Network)
add_subdirectory(build/extensions/Git)
add_subdirectory(build/extensions/LSP)
add_subdirectory(build/extensions/Search)
add_subdirectory(lib/python)
