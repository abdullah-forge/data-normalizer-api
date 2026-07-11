import pandas as pd
import logging
from pathlib import Path
from app.core.name_standardizer import standardizer_name
from app.core.schema_detector import detect_column_schema
from app.core.date_unifier import unify_dates
from app.core.data_cleaner import clean_data
from app.core.reporter import generate_report
from app.utils.memory_profiler import MemoryProfiler

logger = logging.getLogger(__name__)

async def process_file(file_path: Path, original_filename: str) -> dict:
    """
    Yeh function file ko read karega, clean karega, aur report dega.
    """
    profiler = MemoryProfiler()
    profiler.start()
    
    try:
        # STEP 1: File ko Pandas mein load karo (Extension check karo)
        ext = file_path.suffix.lower()
        if ext == '.csv':
            df = pd.read_csv(file_path)
        elif ext in ['.xlsx', '.xls']:
            df = pd.read_excel(file_path)
        elif ext == '.json':
            df = pd.read_json(file_path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")
            
        original_df = df.copy()
        logger.info(f"Loaded {len(df)} rows from {original_filename}")

        df.columns = [standardizer_name(col) for col in df.columns]

        schema = detect_column_schema(df)

        # STEP 4: Dates Unify karo
        df = unify_dates(df, schema)

        # STEP 5: Data Clean karo (Types force karo)
        df = clean_data(df, schema)

        # STEP 6: Report generate karo
        report = generate_report(original_df, df, schema)
        
        # report wala dictionary return kar do
        return report

    except Exception as e:
        logger.error(f"Error processing file: {e}")
        raise
    finally:
        profiler.stop()
