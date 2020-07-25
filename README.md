# properties-file-to-dart-class

Utility Python script to convert a file with extension `.properties` (such as the configuration file `application.properties` in a Java Spring project) or a similar file, to a **Dart** class made of all constant and static strings.

If you don't know what language Dart is, [have a look](https://dart.dev).

## Requirements
**Python 3+**.

## How to run
Run the following command from a CLI:
```bash
python properties_file_to_dart_class.py file_name_with_single_extension.properties
```
Please remove any leading dot, such in `.\file_name_with_single_extension.properties` otherwise the file will be named `.dart` and the class name will be empty (you guess the implementation...or you simply look at the source code).

## Why .properties files?
Because I needed to parse `.properties` files 😎.  
Actually, the only requirement is that rows in the files are in the following format:
```
string_without_spaces=whatever string you like
```
All the rows that the script cannot parse are printed in the console.

## What does the script do?
Few simple things. If you add some more, feel free to fork the repository or post a pull request.  
Here is the script's behaviour:

1. Checks the file existence;
2. Parses the file rows and prints out the rows that will be not carried out;
3. Creates the file content and prints it on a file named after the input file.

If the file is named something like `yo_i-am-a-filename.properties` the output file name will be `yoiamafilename.dart`.
The class name will be simply **yoiamafilename**.

## Example
A file named example_file.properties with this content:
```
test=super test
another test =    value
thisisthe_last  =    will get  trimmed     
```
will become:
```dart
class examplefile {
  static const String test = "super test";
  static const String anothertest = "value";
  static const String thisisthe_last = "will get  trimmed";
}
```