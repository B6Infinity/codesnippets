// ignore_for_file: non_constant_identifier_names, constant_identifier_names

const String tableVARS_ = 'VARS_';

class VAR_Fields {
  static final List<String> values = [
    // All Fields
    id, name, size, max_amt
  ];

  static const String id = '_id';
  static const String name = 'name';
  static const String size = 'size';
  static const String max_amt = 'max_amt';
}

class VAR_ {
  final int? id;
  final String name;
  final int size;
  final int max_amt;

  VAR_({
    this.id,
    required this.name,
    required this.size,
    required this.max_amt,
  });

  Map<String, Object?> toJson() => {
        VAR_Fields.id: id,
        VAR_Fields.name: name,
        VAR_Fields.size: size,
        VAR_Fields.max_amt: max_amt,
      };

  static VAR_ fromJson(Map<String, Object?> json) {
    return VAR_(
      id: int.parse(json[VAR_Fields.id].toString()),
      name: json[VAR_Fields.name] as String,
      size: int.parse(json[VAR_Fields.size] as String),
      max_amt: json[VAR_Fields.max_amt] as int,
    );
  }

  VAR_ copy({
    int? id,
    String? name,
    int? size,
    int? max_amt,
  }) =>
      VAR_(
        id: id ?? this.id,
        name: name ?? this.name,
        size: size ?? this.size,
        max_amt: max_amt ?? this.max_amt,
      );
}
