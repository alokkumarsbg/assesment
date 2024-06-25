import multiprocessing
import logging

logging.basicConfig(level=logging.INFO)

def sum_list(lst):
    return sum(lst)

def perform_addition(lists):
    try:
        with multiprocessing.Pool() as pool:
            results = pool.map(sum_list, lists)
        return results
    except Exception as e:
        logging.error(f"Error performing addition: {str(e)}")
        raise e
