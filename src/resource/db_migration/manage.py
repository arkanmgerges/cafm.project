#!/usr/bin/env python
import os

from migrate.versioning.shell import main

if __name__ == "__main__":
    main(
        repository="src/resource/db_migration",
        url=f'mysql+mysqlconnector://{os.getenv("CAFM_PROJECT_DB_USER", "root")}:{os.getenv("CAFM_PROJECT_DB_PASSWORD", "1234")}@{os.getenv("CAFM_PROJECT_DB_HOST", "127.0.0.1")}:{os.getenv("CAFM_PROJECT_DB_PORT", "3306")}/{os.getenv("CAFM_PROJECT_DB_NAME", "cafm-project")}',
        debug="False",
    )
