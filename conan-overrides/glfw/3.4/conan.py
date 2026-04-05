from conan import ConanFile
from conan.tools.cmake import CMakeToolchain


class GLFWConan(ConanFile):
    name = "glfw"
    version = "3.4"
    settings = "os", "arch", "compiler", "build_type"
    exports_sources = "src/*"  # not used, but keep minimal conformity

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["GLFW_USE_EMSCRIPTEN"] = "ON"
        tc.variables["GLFW_USE_OSMESA"] = "OFF"
        tc.generate()
