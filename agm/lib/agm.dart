/// Support for doing something awesome.
///
/// More dartdocs go here.
library agm;

import 'dart:mirrors';

export 'src/agm_base.dart';

// TODO: Export any libraries intended for clients of this package.

final currentMirror = currentMirrorSystem();
void main(List<String> args) {
  final _local = currentMirror;
}
