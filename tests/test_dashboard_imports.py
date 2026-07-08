from pathlib import Path
import sys
import importlib.util

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))


def test_dashboard_file_exists():
    app_path = BASE_DIR / "dashboard" / "app.py"
    assert app_path.exists()


def test_dashboard_has_valid_python_syntax():
    app_path = BASE_DIR / "dashboard" / "app.py"

    source_code = app_path.read_text(encoding="utf-8")
    compile(source_code, str(app_path), "exec")


def test_core_modules_import_successfully():
    modules = [
        "src.data.load_data",
        "src.models.predict",
        "src.optimization.recommendation_engine",
        "src.optimization.strategy_optimizer",
        "src.utils.helpers",
        "src.visualization.plots",
    ]

    for module in modules:
        imported_module = importlib.import_module(module)
        assert imported_module is not None


def test_streamlit_is_installed():
    streamlit_spec = importlib.util.find_spec("streamlit")
    assert streamlit_spec is not None


def test_dashboard_uses_required_modules():
    app_path = BASE_DIR / "dashboard" / "app.py"
    source_code = app_path.read_text(encoding="utf-8")

    required_imports = [
        "load_processed_data",
        "predict_profit",
        "recommend_strategy",
        "find_best_strategy",
        "format_currency",
        "classify_profit_opportunity",
    ]

    for item in required_imports:
        assert item in source_code