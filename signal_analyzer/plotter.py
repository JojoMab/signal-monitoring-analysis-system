import os
import tempfile
from signal_analyzer.reader import SignalSample


def require_matplotlib():
    matplotlib_config_dir = os.path.join(
        tempfile.gettempdir(),
        "advanced_signal_analyzer_matplotlib",
    )
    os.makedirs(matplotlib_config_dir, exist_ok=True)
    os.environ.setdefault("MPLCONFIGDIR", matplotlib_config_dir)

    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "Plot generation requires matplotlib. Install it with "
            "'python3 -m pip install -r requirements.txt' or run without --plot."
        ) from exc

    return plt


def create_signal_plot(samples: list[SignalSample], output_path: str) -> str:
    plt = require_matplotlib()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    frequencies = [sample.frequency_mhz for sample in samples]
    strengths = [sample.signal_strength_dbm for sample in samples]

    plt.figure()
    plt.plot(frequencies, strengths, marker="o")
    plt.xlabel("Frequency (MHz)")
    plt.ylabel("Signal Strength (dBm)")
    plt.title("Signal Strength by Frequency")
    plt.grid(True)
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()

    return output_path
