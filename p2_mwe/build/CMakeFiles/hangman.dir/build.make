# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/odin/Projekt2/p2_mwe

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/odin/Projekt2/p2_mwe/build

# Include any dependencies generated for this target.
include CMakeFiles/hangman.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/hangman.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/hangman.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/hangman.dir/flags.make

CMakeFiles/hangman.dir/examples/demo_pybind.cpp.o: CMakeFiles/hangman.dir/flags.make
CMakeFiles/hangman.dir/examples/demo_pybind.cpp.o: ../examples/demo_pybind.cpp
CMakeFiles/hangman.dir/examples/demo_pybind.cpp.o: CMakeFiles/hangman.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/odin/Projekt2/p2_mwe/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/hangman.dir/examples/demo_pybind.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/hangman.dir/examples/demo_pybind.cpp.o -MF CMakeFiles/hangman.dir/examples/demo_pybind.cpp.o.d -o CMakeFiles/hangman.dir/examples/demo_pybind.cpp.o -c /home/odin/Projekt2/p2_mwe/examples/demo_pybind.cpp

CMakeFiles/hangman.dir/examples/demo_pybind.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/hangman.dir/examples/demo_pybind.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/odin/Projekt2/p2_mwe/examples/demo_pybind.cpp > CMakeFiles/hangman.dir/examples/demo_pybind.cpp.i

CMakeFiles/hangman.dir/examples/demo_pybind.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/hangman.dir/examples/demo_pybind.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/odin/Projekt2/p2_mwe/examples/demo_pybind.cpp -o CMakeFiles/hangman.dir/examples/demo_pybind.cpp.s

# Object files for target hangman
hangman_OBJECTS = \
"CMakeFiles/hangman.dir/examples/demo_pybind.cpp.o"

# External object files for target hangman
hangman_EXTERNAL_OBJECTS =

hangman.cpython-310-x86_64-linux-gnu.so: CMakeFiles/hangman.dir/examples/demo_pybind.cpp.o
hangman.cpython-310-x86_64-linux-gnu.so: CMakeFiles/hangman.dir/build.make
hangman.cpython-310-x86_64-linux-gnu.so: CMakeFiles/hangman.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/odin/Projekt2/p2_mwe/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared module hangman.cpython-310-x86_64-linux-gnu.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/hangman.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/hangman.dir/build: hangman.cpython-310-x86_64-linux-gnu.so
.PHONY : CMakeFiles/hangman.dir/build

CMakeFiles/hangman.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/hangman.dir/cmake_clean.cmake
.PHONY : CMakeFiles/hangman.dir/clean

CMakeFiles/hangman.dir/depend:
	cd /home/odin/Projekt2/p2_mwe/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/odin/Projekt2/p2_mwe /home/odin/Projekt2/p2_mwe /home/odin/Projekt2/p2_mwe/build /home/odin/Projekt2/p2_mwe/build /home/odin/Projekt2/p2_mwe/build/CMakeFiles/hangman.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/hangman.dir/depend

