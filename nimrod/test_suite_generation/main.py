import logging
from typing import List

from nimrod.test_suite_generation.generators.test_suite_generator import TestSuiteGenerator
from nimrod.test_suite_generation.test_suite import TestSuite
from nimrod.core.merge_scenario_under_analysis import MergeScenarioUnderAnalysis


class TestSuiteGeneration:
    def __init__(self, test_suite_generators: List[TestSuiteGenerator]) -> None:
        self._test_suite_generators = test_suite_generators

    def generate_test_suites(self, scenario: MergeScenarioUnderAnalysis, input_jar: str, use_determinism: bool) -> List[TestSuite]:
        f = open("/Users/hugoalvescardoso/Desktop/SMAT/SMAT/nimrod/test_suite_generation/logging_file.txt","a")
        logging.info("Starting tests generation for project %s using jar %s", scenario.project_name, input_jar)
        f.write(f"INFO main - Starting tests generation for project {scenario.project_name} using jar {input_jar} \n")
        test_suites: List[TestSuite] = list()

        for generator in self._test_suite_generators:
            try:
                test_suites.append(generator.generate_and_compile_test_suite(
                    scenario, input_jar, use_determinism))
            except Exception as error:
                logging.error(f"It was not possible to generate test suite using {generator.get_generator_tool_name()}")
                logging.debug(error)
                f.write("ERROR main - It was not possible to generate test suite using "+str(generator.get_generator_tool_name())+"\n")
                f.write("DEBUG main - "+str(error)+'\n')

        logging.info("Finished tests generation for project %s using jar %s", scenario.project_name, input_jar)
        f.write("INFO main - Finished tests generation for project "+str(scenario.project_name)+"using jar "+str(input_jar)+"\n")
        f.close()
        return test_suites
