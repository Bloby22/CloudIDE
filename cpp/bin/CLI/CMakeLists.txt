add_executable(CLI src/main.cpp)
target_include_directories(CLI PRIVATE
    ${CMAKE_SOURCE_DIR}/build/core/Engine/include
    ${CMAKE_SOURCE_DIR}/build/system/Terminal/include
    ${nlohmann_json_SOURCE_DIR}/include
)
target_link_libraries(CLI PRIVATE Engine Terminal nlohmann_json::nlohmann_json)
set_target_properties(CLI PROPERTIES OUTPUT_NAME "CLI")
install(TARGETS CLI RUNTIME DESTINATION ${INSTALL_BIN})
