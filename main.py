from db.connection import get_connection
from utility.file_utils import get_dir_filnames

def run():
    filepaths = get_dir_filnames('./exported')
    conn = get_connection()

    for f in filepaths:
        with open(f, 'r', encoding='utf-8-sig' ) as f:
            json_geofences = f.readlines()

            # exec procedure

    conn.close()

if __name__ == '__main__':
    run()