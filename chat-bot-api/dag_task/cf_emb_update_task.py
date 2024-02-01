import numpy as np
import os

from dag.task import python_thesis_operator


os.environ['BASE_PATH']         = f'{os.environ["HOME"]}/development/personal/maestria/thesis-paper'
os.environ['TMP_PATH']         = f'{os.environ["BASE_PATH"]}/tmp'
os.environ['DATASET_PATH']     = f'{os.environ["BASE_PATH"]}/datasets'
os.environ['WEIGHTS_PATH']     = f'{os.environ["BASE_PATH"]}/weights'
os.environ['METRICS_PATH']     = f'{os.environ["BASE_PATH"]}/metrics'
os.environ['MONGODB_URL']      = 'mongodb://0.0.0.0:27017'
os.environ['MONGODB_DATABASE'] = 'chatbot'
os.environ['CHROMA_HOST']      = '0.0.0.0'
os.environ['CHROMA_PORT']      = '9090'


def python_callable(**ctx):
    import sys
    sys.path.append(f'{ctx["thesis.src_path"]}')
    sys.path.append(f'{ctx["thesis.src_path"]}/../chat-bot-api')
    from app_context import AppContext

    AppContext().cf_emb_update_job()


def cf_emb_update_task(dag, task_id='cf_emb_update_task'):
    return python_thesis_operator(
        dag,
        task_id,
        python_callable,
        params={}
    )
