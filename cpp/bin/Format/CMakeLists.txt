add_executable(Format src/main.cpp)
target_include_directories(Format PRIVATE
    ${CMAKE_SOURCE_DIR}/build/core/Engine/include
    ${CMAKE_SOURCE_DIR}/build/system/Terminal/include
    ${nlohmann_json_SOURCE_DIR}/include
)
target_link_libraries(Format PRIVATE Engine Terminal nlohmann_json::nlohmann_json)
set_target_properties(Format PROPERTIES OUTPUT_NAME "Format")
install(TARGETS Format RUNTIME DESTINATION ${INSTALL_BIN})
