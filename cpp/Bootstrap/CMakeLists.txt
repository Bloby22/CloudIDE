add_executable(Bootstrap src/bootstrap.cpp)
target_include_directories(Bootstrap PRIVATE
    ${CMAKE_SOURCE_DIR}/build/system/Network/include
    ${nlohmann_json_SOURCE_DIR}/include
)
target_link_libraries(Bootstrap PRIVATE Network Reproc)
if(WIN32)
    target_link_libraries(Bootstrap PRIVATE urlmon)
endif()
set_target_properties(Bootstrap PROPERTIES OUTPUT_NAME "Bootstrap")
install(TARGETS Bootstrap RUNTIME DESTINATION ${CMAKE_SOURCE_DIR}/dist)
