find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG REQUIRED)

set(PYINSTALL ${INSTALL_LIB}/python)

pybind11_add_module(API src/API.cpp)
target_include_directories(API PRIVATE ${CMAKE_SOURCE_DIR}/build/core/Engine/include)
target_link_libraries(API PRIVATE pybind11::module Engine)
set_target_properties(API PROPERTIES OUTPUT_NAME "API" PREFIX "" SUFFIX ".pyd")
install(TARGETS API LIBRARY DESTINATION ${PYINSTALL})

pybind11_add_module(Core src/Core.cpp)
target_include_directories(Core PRIVATE ${CMAKE_SOURCE_DIR}/build/core/Engine/include)
target_link_libraries(Core PRIVATE pybind11::module Engine)
set_target_properties(Core PROPERTIES OUTPUT_NAME "Core" PREFIX "" SUFFIX ".pyd")
install(TARGETS Core LIBRARY DESTINATION ${PYINSTALL})

pybind11_add_module(Nodes src/Nodes.cpp)
target_include_directories(Nodes PRIVATE ${CMAKE_SOURCE_DIR}/build/core/Engine/include)
target_link_libraries(Nodes PRIVATE pybind11::module Engine)
set_target_properties(Nodes PROPERTIES OUTPUT_NAME "Nodes" PREFIX "" SUFFIX ".pyd")
install(TARGETS Nodes LIBRARY DESTINATION ${PYINSTALL})
