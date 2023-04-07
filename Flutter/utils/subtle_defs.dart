import 'package:flutter/material.dart';

Widget h3txt(String txt,
    {int multiplier = 1, Color? color, double padding = 8.0}) {
  return Padding(
    padding: EdgeInsets.all(padding),
    child: Text(
      txt,
      style: TextStyle(
        fontSize: (22 * multiplier).toDouble(),
        fontWeight: FontWeight.bold,
        color: color,
      ),
    ),
  );
}

Widget h3heading(String txt,
    {int multiplier = 1,
    alignment = MainAxisAlignment.center,
    Color? color,
    double padding = 8.0}) {
  return Row(
    mainAxisAlignment: alignment,
    children: [
      Padding(
        padding: EdgeInsets.all(padding),
        child: Text(
          txt,
          style: TextStyle(
            fontSize: (20 * multiplier).toDouble(),
            fontWeight: FontWeight.bold,
            color: color,
          ),
        ),
      ),
    ],
  );
}
