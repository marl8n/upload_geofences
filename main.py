from db.connection import get_connection
from utility.file_utils import get_dir_filnames


def run():
    filepaths = get_dir_filnames("./exported")
    conn = get_connection()
    cursor = conn.cursor()
    stored_proc_name = "spWT_Geofences_ImportGeofenceByJson"

    try:
        for f in filepaths:
            with open(f, "r", encoding="utf-8-sig") as f:
                json_geofences = f.readlines()

                # exec procedure
                cursor.execute(
                    f"""
                    EXEC {stored_proc_name}
                        @userId=-1,
                        @organizationId=?,
                        @jsonList='{json_geofences}'
                    """
                )

    except Exception as e:
        print(e)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    run()
