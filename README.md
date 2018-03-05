## g2p Run Information Database

Run information database for Jefferson Lab experiment E08-027 (g2p).

Originally developed by R. Zielinski (See [g2pwiki](https://hallaweb.jlab.org/wiki/index.php/G2pmysql) for more details).

Converted to sqlite format for convenience.

### How to update g2p.db

1. Dump the g2p mySQL database from the server:
```
mysqldump --compatible=ansi --skip-extended-insert --compact --single-transaction -h [SERVER] -u [USER] -p [PASSWORD] g2p > g2p.sql
```
2. Download the script [mysql2sqlite](https://github.com/dumblob/mysql2sqlite.git), convert g2p.sql to sqlite format:
```
./mysql2sqlite g2p.sql | sqlite3 g2p.db
```
