add_executable(LSP src/main.cpp)
target_include_directories(LSP PRIVATE
    ${CMAKE_SOURCE_DIR}/build/core/Engine/include
    ${CMAKE_SOURCE_DIR}/build/system/Terminal/include
    ${nlohmann_json_SOURCE_DIR}/include
)
target_link_libraries(LSP PRIVATE Engine Terminal nlohmann_json::nlohmann_json)
set_target_properties(LSP PROPERTIES OUTPUT_NAME "LSP")
install(TARGETS LSP RUNTIME DESTINATION ${INSTALL_BIN})
