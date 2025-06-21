import argostranslate.package
import argostranslate.translate

# List of language pairs you want to support
LANGUAGE_PAIRS = [
    ("en", "es"),  # English <-> Spanish
    ("en", "fr"),  # English <-> French
    ("en", "de"),  # English <-> German
    # Add more as needed
]

def ensure_models_installed():
    # Update index and fetch available packages
    argostranslate.package.update_package_index()
    packages = argostranslate.package.get_available_packages()

    for from_code, to_code in LANGUAGE_PAIRS:
        for package in packages:
            if (package.from_code == from_code and package.to_code == to_code):
                print(f"Installing model for {from_code} -> {to_code}...")
                download_path = argostranslate.package.download_package(package)
                argostranslate.package.install_from_path(download_path)
                break  # Install only one matching package per pair

# Ensure translation models are ready before starting app
ensure_models_installed()

# Now import and launch LibreTranslate
from libretranslate.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
