# Changelog

All notable changes to autocsv-profiler-suite will be documented in this file.

## [2.0.0] - 2025-09-28

### Added

- Unified orchestrator `bin/run_analysis.py` for cross-platform execution
- BaseProfiler abstract class for consistent engine interface
- Configuration system with `config/master_config.yml` as single source of truth
- Environment manager `bin/setup_environments.py` for parallel/sequential setup
- Rich console interface with progress tracking and formatted output
- Interactive file selection with path validation and encoding detection
- Engine selection menu with multi-select capability
- Column exclusion workflow in main engine
- Visualization selection interface for plot generation
- Automatic memory management with chunking for files over 50MB
- Parallel visualization processing with multiprocessing
- Structural delimiter detection algorithm
- TableOne analysis for grouped statistics
- Dataset info module for comprehensive data analysis
- Documentation: ARCHITECTURE.md, DEVELOPMENT.md, USER_GUIDE.md, TROUBLESHOOTING.md
- API documentation in docs/api/ directory
- Engine testing guide for isolated environment testing

### Changed

- Entry point from batch scripts to `python bin/run_analysis.py`
- Package structure reorganized as `autocsv_profiler` module
- Multi-environment architecture with subprocess isolation
- Performance improved 20-30% with pandas 2.3.1 and numpy 2.2.6
- Data loading uses automatic chunking strategy based on file size
- Memory monitoring with real-time tracking
- Interactive workflow with step-by-step guidance
- Error messages provide user-friendly solutions
- Path display uses truncation for cleaner console output
- Debug mode available with `--debug` flag

### Deprecated

- Batch file entry points (run_analysis.bat, run_analysis.sh)
- Individual script imports replaced by package imports

### Removed

- Platform-specific batch scripts
- Scattered configuration files replaced by master config

### Fixed

- Windows console encoding now properly handles UTF-8
- Matplotlib backend conflicts resolved with forced Agg backend
- Progress bar interference with subprocess execution
- Memory leaks through process isolation
- Import conflicts between engines

### Security

- Path validation prevents directory traversal
- Delimiter validation blocks dangerous characters
- Memory limits prevent resource exhaustion

## [v1.1.0] - 2025-08-04

### Changed

- **Environment System**: Migrated from virtual environments to conda environments for better dependency management
- **Environment Names**: Renamed environments for clarity:
  - `ds_ml` → `csv-profiler-main`
  - `sweetz_ydata_profiler` → `csv-profiler-profiling`
  - `dataprep` → `csv-profiler-dataprep`
- **Python Versions**: Updated to Python 3.11.7 for main environment, 3.10.4 for profiling tools
- **Dependencies**: Replaced requirements.txt with conda environment.yml files
- **Project Structure**: Reorganized to follow Python packaging standards

### Added

- Interactive environment manager (`setup_environments.ps1`)
- Documentation with workflow diagrams
- Legal documentation (LICENSE, NOTICE files)
- Environment status display and management tools
- Source file license headers for MIT License compliance
- Multi-environment exclusive focus (removed PyPI package references)

### Improved

- **Dependency Management**: Eliminated package conflicts through conda isolation
- **Installation Process**: Environment setup through conda
- **Documentation**: Added visual guides with mermaid diagrams
- **Error Handling**: Better user feedback and troubleshooting guidance
- **Code Quality**: Removed auto-installation code for more reliable execution

### Fixed

- Package version conflicts between profiling tools
- Environment activation reliability on Windows systems
- Consistent package versions across installations

## [v1.0.0] - 2025-04-09

### Added

- Initial release with virtual environment support
- Core analysis modules:
  - `auto_csv_profiler.py` - Comprehensive statistical analysis
  - `profile_ydata_profiling_report.py` - YData profiling reports
  - `profile_sweetviz_report.py` - SweetViz visual reports
  - `profile_dataprep_report.py` - DataPrep EDA reports
  - `recognize_delimiter.py` - Automatic delimiter detection
- Batch orchestration script (`run_analysis.bat`)
- Three specialized conda environments plus base environment for tool execution
- Output artifacts (HTML reports, visualizations, cleaned data)
- Sample dataset and example outputs
- MIT License

### Features

- Automated CSV analysis workflow
- Multiple profiling engines integration
- Interactive user prompts for customization
- Cross-platform path handling
- Statistical analysis and visualization suite
