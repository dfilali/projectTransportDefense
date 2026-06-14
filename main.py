
from pipelines.main_pipeline import MainPipeline

def main():
    print("🚆 Urban Mobility Intelligence System Starting...")
    pipeline = MainPipeline()
    pipeline.run()
    print("✅ Pipeline finished")

if __name__ == "__main__":
    main()
