from unittest import TestCase

from nimrod.tests.utils import get_config
from nimrod.tools.java import Java
from nimrod.tools.jacoco import Jacoco


class TestJacoco(TestCase):

    @classmethod
    def setUp(cls):
        cls.java_home = get_config()['java_home']
        cls.java = Java(cls.java_home)
        cls.jacoco = Jacoco(cls.java)

    # Teste do comando java -jar jacococli.jar instrument "jar_a_ser_modificado" --dest "local_jar_instrumentado"
    def test_instrument(self):

        jarSemModificacaoes = "/home/vinicius/Documentos/UFPE/TCC/mergedataset/cloud-slang/20bac30d9bd76569aa6a4fa1e8261c1a9b5e6f76/original/base/cloudslang-all-0.7.50-SNAPSHOT-jar-with-dependencies.jar"
        destinoJarInstrumentado = "/home/vinicius/Documentos/UFPE/TCC/Resultados/CloudSlang/cloudslang-all/dest"

        self.jacoco.execInstrumentJar(jarSemModificacaoes, destinoJarInstrumentado)

    def test_runTest(self):

        projectJar = "/home/vinicius/Documentos/UFPE/TCC/Resultados/CloudSlang/cloudslang-all/dest/cloudslang-all-0.7.50-SNAPSHOT-jar-with-dependencies.jar"
        suiteClass = "/home/vinicius/Documentos/UFPE/TCC/Resultados/CloudSlang/cloudslang-all/Class/"
        test_class = "RegressionTest0"

        self.jacoco.createJacocoExec(projectJar, suiteClass, test_class)

    def test_generateReport(self):
        jacocoExecDir = "/home/vinicius/Documentos/UFPE/TCC/SMAT/nimrod/tests/tools/jacoco.exec"
        classFile = "/home/vinicius/Documentos/UFPE/TCC/Projetos/cloud-slang/cloudslang-all/target/classes/io/cloudslang/lang/api"
        csvFile = "/home/vinicius/Documentos/UFPE/TCC/Resultados/CloudSlang/cloudslang-all/dest/report.csv"

        self.jacoco.generateReport(jacocoExecDir, classFile, csvFile)
