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
      suites_3 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.left, use_determinism, 3)
      suites_30 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 30)
      suites_33 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 33)
      suites_300 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 300)
      suites_303 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 303)
      suites_333 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 333)
      suites_3000 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 3000)
      suites_3003 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 3003)
      suites_3030 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 3030)
      suites_3033 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 3033)
      suites_3300 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 3300)
      suites_3303 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 3303)
      suites_3330 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 3330)
      suites_3333 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 3333)

      return suites_3 + suites_30 + suites_33 + suites_300 + suites_303 + suites_333 + suites_3000 + suites_3003 + suites_3030 + suites_3033 + suites_3300 + suites_3303 + suites_3330 + suites_3333
