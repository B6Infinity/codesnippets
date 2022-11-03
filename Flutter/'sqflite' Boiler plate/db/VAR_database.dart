// import 'package:__APPNAME__/model/VAR_.dart';
import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';

class VARS_Database {
  static final VARS_Database instance = VARS_Database._init();

  static Database? _database;

  VARS_Database._init();

  Future<Database> get database async {
    if (_database != null) return _database!;

    _database = await _initDB('VARS_.db');
    return _database!;
  }

  Future<Database> _initDB(String filepath) async {
    final dbPath = await getDatabasesPath();
    final path = join(dbPath, filepath);

    return await openDatabase(path, version: 1, onCreate: _createDB);
  }

  Future _createDB(Database db, int version) async {
    const idType = 'INTEGER PRIMARY KEY AUTOINCREMENT';
    const boolType = 'BOOLEAN NOT NULL';
    const intType = 'INTEGER NOT NULL';
    const stringType = 'TEXT NOT NULL';
    const listType = 'LIST NOT NULL';

    await db.execute('''CREATE TABLE $tableVARS_ (

      ${VAR_Fields.id} $idType,
      ${VAR_Fields.name} $stringType,
      ${VAR_Fields.bg_color} $stringType,
      ${VAR_Fields.txt_color} $stringType,
      ${VAR_Fields.size} $stringType,
      ${VAR_Fields.max_amt} $intType,
      ${VAR_Fields.present_amt} $intType


    )''');

    // https://www.youtube.com/watch?v=UpKrhZ0Hppk&t=293s&ab_channel=JohannesMilke
  }

  Future close() async {
    final db = await instance.database;
    db.close();
  }

  // '''     CRUD       '''

  Future<VAR_> create(VAR_ VAR_) async {
    final db = await instance.database;

    final id = await db.insert(tableVARS_, VAR_.toJson());
    return VAR_.copy(id: id);
  }

  Future<VAR_?> readVAR_(int id) async {
    final db = await instance.database;

    final maps = await db.query(
      tableVARS_,
      columns: VAR_Fields.values,
      where: '${VAR_Fields.id} = ?',
      whereArgs: [id],
    );

    if (maps.isNotEmpty) {
      return VAR_.fromJson(maps.first);
    } else {
      // throw Exception('VAR_ $id not found');
      return null;
    }
  }

  Future<List<VAR_>> readAllVARS_() async {
    final db = await instance.database;

    final result = await db.query(tableVARS_);

    return result.map((json) => VAR_.fromJson(json)).toList();
    // ORDER BY　とか ?? https://youtu.be/UpKrhZ0Hppk?t=1189
  }

  Future<int> updateVAR_(int id, VAR_ VAR_) async {
    final db = await instance.database;

    return db.update(
      tableVARS_,
      VAR_.toJson(),
      where: '${VAR_Fields.id} = ?',
      whereArgs: [id],
    );
  }

  Future<int> deleteVAR_(int id) async {
    final db = await instance.database;

    return await db.delete(
      tableVARS_,
      where: '${VAR_Fields.id} = ?',
      whereArgs: [id],
    );
  }
}
