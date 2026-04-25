# Web GUIs in C++?

Included in the long the long list of tasks that were historically difficult
were C++ GUIs and should immediately come to mind a short list of difficult options.

- **CGI**: OLD SCHOOL; html tag printing, that still requires CSS/JS to make it pretty
  and has vulnerabilities of responding to web request from an executable. Oh, and
  its only web.
- **Wt** (Webtoolkit): WEB ONLY; a fair option but few examples of production
  applications, licensing concerns for commercialization.
- **Qt**: Desktop focused with WASM; licensing concerns the output becomes
  commercial, some web support
  for WASM but the executables are heavy and
- **IM_GUI** BARE BONES; Open source, WASM ready or adaptable
  requires writing EVERYTHING FROM SCRATCH...

However, there is a new option:

- **hello_imgui** open source, portable and cross environment ready;
  one source code that runs everywhere, native desktop and browser and potentially
  in browser extensions and comes with widgets/examples.

This is still an on going experiment and if one is reading this than

## TOC
