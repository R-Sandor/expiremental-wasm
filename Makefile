.PHONY: conan_default conan_wasm 

default: 
	$(MAKE) conan_default

conan_default:
	conan install . --profile:build=default --build=missing

conan_wasm:
	conan install . --profile:build=default --profile:host=conan-profiles/emscripten.profile --build=missing

