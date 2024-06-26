# Configuration

SMAT allows the user to configure some aspects of its execution. This can be done by editing the [nimrod/tests/env-config.json](../nimrod/tests/env-config.json) file. This session will discuss the available options for customization.

## General
The following properties are related to general behavior of SMAT.

### java_home
By default, SMAT will use the `JAVA_HOME` env var to populate Java Home. However, it's possible to override this value by setting the `java_home` property in the configuration file.

### maven_home
By default, SMAT will use either `MAVEN_HOME` or `MVN_HOME`, in this particular order, to populate Maven Home. However, it's possible to override this value by setting the `maven_home` property in the configuration file.

### logger_level
This property allows to change the minimum level of logging messages which are shown during execution. The default value is `INFO`, but can be customized to either: `CRITICAL`, `ERROR`, `WARNING`, `INFO` or `DEBUG`.

### input_path
This property contains a path to the JSON file which contains input scenarios for SMAT. Please refer to the input documentation for more information regarding the input format.

## Test Suite Generation
The following properties are related to the Test Suites Generation step.

### test_suite_generators
This property consists of an array with the name of the Generators which will be used in SMAT during Test Suite Generation step. If not set, all the implemented generators will be used. Valid values are: `randoop`, `randoop-modified`, `evosuite`, `evosuite-differential` and `project`.

### test_suite_generation_search_time_available
This property is only used if deterministic test suite generation is disabled. It allows to customize the time **in seconds** provided for each generator during Test Suite Generation. Default value is 300 seconds.

### test_suite_generation_deterministic_tests_quantity
This property is only used if deterministic test suite generation is enabled. When using deterministic test suite generation, the time for search available cannot be used as a stopping criteria, since different computing power can influence in the time required to generate the same test suite. Thus, SMAT uses the total number of tests generated as a stopping criteria for each one of its generators. By assigning this property, it's possible to customize the total number of tests that are generated by each generator. Default value is 100_000_000.

### generate_deterministic_test_suites
If set to true, SMAT will use deterministic versions of its generators, i.e., the generated suites will always be the same regardless of how many times the code is executed.

### test_suite_generation_seed
When `generate_deterministic_test_suites` is set to true, the user customizes the seed that is provided for the invoked test generation tools. Default value is `42`.

## Output Generation
The following properties are related to the Output Generation step.

### output_generators
This property consists of an array with the name of the Reports that are going to be written during the Output Generation step. If not set, all the implemented generators will be used. Valid values are: `behavior_changes`, `semantic_conflicts`, `test_suites`.
