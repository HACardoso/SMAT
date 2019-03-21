/*
 * This file was automatically generated by EvoSuite
 * Sat Mar 16 14:19:06 GMT 2019
 */

package org.apache.commons.lang;

import org.junit.Test;
import static org.junit.Assert.*;
import org.apache.commons.lang.WordUtils;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true, useJEE = true) 
public class WordUtils_ESTest extends WordUtils_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      String string0 = "6.0";
      String string1 = WordUtils.wrap("6.0", (-2400));
      assertEquals("6.0", string1); // (Primitive) Original Value: 6.0 | Regression Value: 0
      assertTrue(string1.equals((Object)string0));
  }
}