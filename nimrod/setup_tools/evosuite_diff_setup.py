from nimrod.core.merge_scenario_under_analysis import MergeScenarioUnderAnalysis
from nimrod.setup_tools.setup_tool import Setup_tool
from nimrod.test_suite_generation.generators.evosuite_differential_test_suite_generator import EvosuiteDifferentialTestSuiteGenerator
from nimrod.tests.utils import get_config


class Evosuite_Diff_setup(Setup_tool):

    def generate_test_suite(self, scenario, project_dep, input: MergeScenarioUnderAnalysis = None):
        use_determinism = bool(get_config().get('generate_deterministic_test_suites', False))
        evosuite_diff = EvosuiteDifferentialTestSuiteGenerator(project_dep.java)
        new_suite = evosuite_diff.generate_and_compile_test_suite(input, project_dep.parentReg, use_determinism)
        self.test_suite = self._convert_new_suite_to_old_test_suite(new_suite)
        return self.test_suite