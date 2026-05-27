add_executable(Launcher src/main.cpp)
target_include_directories(Launcher PRIVATE
    ${CMAKE_SOURCE_DIR}/build/core/Engine/include
    ${CMAKE_SOURCE_DIR}/build/system/Terminal/include
    ${nlohmann_json_SOURCE_DIR}/include
)
target_link_libraries(Launcher PRIVATE Engine Terminal Network)
set_target_properties(Launcher PROPERTIES OUTPUT_NAME "Launcher")
install(TARGETS Launcher  RUNTIME DESTINATION ${CMAKE_SOURCE_DIR}/dist)
