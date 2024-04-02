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
      lst = []


      suites_3 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.left, use_determinism, 3)
      lst.append(suites_3)
      suites_30 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 30)
      lst.append(suites_30)
      suites_33 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 33)
      lst.append(suites_33)
      suites_300 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 300)
      lst.append(suites_300)
      suites_303 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 303)
      lst.append(suites_303)
      suites_333 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 333)
      lst.append(suites_333)
      suites_3000 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 3000)
      lst.append(suites_3000)
      suites_3003 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 3003)
      lst.append(suites_3003)
      suites_3030 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 3030)
      lst.append(suites_3030)
      suites_3033 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 3033)
      lst.append(suites_3033)
      suites_3300 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 3300)
      lst.append(suites_3300)
      suites_3303 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 3303)
      lst.append(suites_3303)
      suites_3330 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 3330)
      lst.append(suites_3330)
      suites_3333 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 3333)
      lst.append(suites_3333)
      suites_30000 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 30000)
      lst.append(suites_30000)
      suites_30003 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 30003)
      lst.append(suites_30003)
      suites_30030 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 30030)
      lst.append(suites_30030)
      suites_30033 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 30033)
      lst.append(suites_30033)
      suites_30300 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 30300)
      lst.append(suites_30300)
      suites_30303 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 30303)
      lst.append(suites_30303)
      suites_30330 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 30330)
      lst.append(suites_30330)
      suites_30333 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 30333)
      lst.append(suites_30333)
      suites_33000 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 33000)
      lst.append(suites_33000)
      suites_33003 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 33003)
      lst.append(suites_33003)
      suites_33003 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 33003)
      lst.append(suites_33003)
      suites_33030 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 33030)
      lst.append(suites_33030)
      suites_33033 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 33033)
      lst.append(suites_33033)
      suites_33300 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 33300)
      lst.append(suites_33300)
      suites_33303 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 33303)
      lst.append(suites_33303)
      suites_33330 = self._test_suite_generation.generate_test_suites(scenario, scenario.scenario_jars.right, use_determinism, 33330)
      lst.append(suites_33330)

      return lst