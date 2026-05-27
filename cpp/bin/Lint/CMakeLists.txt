add_executable(Lint src/main.cpp)
target_include_directories(Lint PRIVATE
    ${CMAKE_SOURCE_DIR}/build/core/Engine/include
    ${CMAKE_SOURCE_DIR}/build/system/Terminal/include
    ${nlohmann_json_SOURCE_DIR}/include
)
target_link_libraries(Lint PRIVATE Engine Terminal nlohmann_json::nlohmann_json)
set_target_properties(Lint PROPERTIES OUTPUT_NAME "Lint")
install(TARGETS Lint RUNTIME DESTINATION ${INSTALL_BIN})
