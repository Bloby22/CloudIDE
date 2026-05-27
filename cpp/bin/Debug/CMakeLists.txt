add_executable(Debug src/main.cpp)
target_include_directories(Debug PRIVATE
    ${CMAKE_SOURCE_DIR}/build/core/Engine/include
    ${CMAKE_SOURCE_DIR}/build/system/Terminal/include
    ${nlohmann_json_SOURCE_DIR}/include
)
target_link_libraries(Debug PRIVATE Engine Terminal nlohmann_json::nlohmann_json)
set_target_properties(Debug PROPERTIES OUTPUT_NAME "Debug")
install(TARGETS Debug RUNTIME DESTINATION ${INSTALL_BIN})
