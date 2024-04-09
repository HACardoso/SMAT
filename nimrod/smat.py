from typing import List

from nimrod.dynamic_analysis.main import DynamicAnalysis
from nimrod.core.merge_scenario_under_analysis import MergeScenarioUnderAnalysis
from nimrod.output_generation.output_generator import OutputGenerator, OutputGeneratorContext
from nimrod.test_suite_generation.main import TestSuiteGeneration
from nimrod.test_suite_generation.test_suite import TestSuite
from nimrod.test_suites_execution.main import TestSuitesExecution
from nimrod.tests.utils import get_config


class SMAT:
  def __init__(self, test_suite_generation: TestSuiteGeneration, test_suites_execution: TestSuitesExecution, dynamic_analisys: DynamicAnalysis, output_generators: List[OutputGenerator]) -> None:
    self._test_suite_generation = test_suite_generation
    self._test_suites_execution = test_suites_execution
    self._dynamic_analysis = dynamic_analisys
    self._output_generators = output_generators

  def run_tool_for_semmantic_conflict_detection(self, scenario: MergeScenarioUnderAnalysis) -> None:
    test_suites = self._generate_test_suites_for_scenario(scenario)
    executions = self._test_suites_execution.execute_test_suites(test_suites, scenario.scenario_jars)
    semantic_conflicts = self._dynamic_analysis.check_for_semantic_conflicts(executions)    
    behavior_changes = self._dynamic_analysis.check_for_behavior_changes(executions)

    for output_generator in self._output_generators:
      output_generator.write_report(OutputGeneratorContext(
          scenario=scenario,
          test_suites=test_suites,
          test_case_executions=executions,
          semantic_conflicts=semantic_conflicts,
          behavior_changes=behavior_changes
      ))
  
  def _generate_test_suites_for_scenario(self, scenario: MergeScenarioUnderAnalysis) -> List[TestSuite]:
      
      use_determinism = bool(get_config().get('generate_deterministic_test_suites', False))


      suites_1 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.left, use_determinism, 1)
      suites_2 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 2)
      suites_3 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 3)
      suites_4 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 4)
      suites_5 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 5)
      suites_6 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 6)
      suites_7 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 7)
      suites_8 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 8)
      suites_9 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 9)
      suites_10 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 10)
      #suites_11 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 11)
      #suites_12 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 12)
      #suites_13 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 13)
      #suites_14 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 14)
      #suites_15 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 15)
      #suites_16 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 16)
      #suites_17 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 17)
      #suites_18 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 18)
      #suites_19 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 19)
      #suites_20 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 20)
      #suites_21 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 21)
      #suites_22 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 22)
      #suites_23 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 23)
      #suites_24 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 24)
      #suites_25 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 25)
      #suites_26 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 26)
      #suites_27 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 27)
      #suites_28 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 28)
      #suites_29 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 29)
      #suites_30 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 30)
      

      return suites_1 + suites_2 + suites_3 + suites_4 + suites_5 + suites_6 + suites_7 + suites_8 + suites_9 + suites_10