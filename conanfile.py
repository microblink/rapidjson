from conans import ConanFile, CMake, tools


class RapidJSONConan(ConanFile):
    name = "RapidJSON"
    version = "1.1.1"
    license = "BSD"
    url = "https://github.com/microblink/rapidjson"
    description = "A fast JSON parser/generator for C++ with both SAX/DOM style API"
    generators = "cmake"
    scm = {
        "type": "git",
        "url": "auto",
        "revision": "auto"
    }
    no_copy_source = True


    def package(self):
        self.copy("include/*.h", dst="")


    def package_id(self):
        self.info.header_only()

