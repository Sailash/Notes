from datetime import datetime, timedelta
from airflow import DAG
from airflow.timetables.base import Timetable, DagRunInfo, DataInterval


class Every5Min(Timetable):
    def infer_manual_data_interval(self, run_after):
            return DataInterval(start=run_after, end=run_after)

                def next_dagrun_info(self, last_automated_data_interval, restriction):
                        if last_automated_data_interval is None:
                                    start = restriction.earliest
                                            else:
                                                        start = last_automated_data_interval.end

                                                                next_start = start + timedelta(minutes=5)
                                                                        return DagRunInfo.interval(next_start, next_start + timedelta(minutes=5))


                                                                        with DAG(
                                                                            dag_id="every_5min_example",
                                                                                start_date=datetime(2024, 1, 1),
                                                                                    timetable=Every5Min(),
                                                                                        catchup=False,
                                                                                        ):
                                                                                            from airflow.operators.empty import EmptyOperator
                                                                                                EmptyOperator(task_id="run")
                                                                                                