import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    report_melted = pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')
    return report_melted

    