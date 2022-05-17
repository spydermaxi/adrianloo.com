Caller Dispatch - Python
########################

:date: 2022-03-04 22:50
:tags: caller dispatch, if else statements, python, dictionary, dispatch, functions, conditional logic, function call
:slug: caller-dispatch-to-replace-ifelse
:authors: Adrian Loo
:lang: en
:feature_image: images/caller_dispatch_adrianloo.jpg
:summary: Python - Using caller dispatch or dispatch table to replace if else statements. In this article, I share how we can use dispatch tables to replace if else statements when calling different functions base on specifc logics


Let's say there are four XML files with different element structures.
In order to parse all four files into a specifc dataframe structure as shown below, we need to write specifc functions to read different level of elements in each xml file.

.. code-block:: python

   # Example dataframe:
   numpy_data = np.array([[1, 2, 3]])
   df = pd.DataFrame(data=numpy_data, columns=['Category', 'Key', 'Value'])
   print(df)

      Category  Key  Value
   0         1    2      3

Writing the individual functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since all xml files has different element structures, the method to parse those files are different.

.. code-block:: python

   def parse_syscfg(xml_file):
       root = ET.parse(xml_file).getroot()
       param_ls = []
       for i in root:
           for c in i:
               param_ls.append({'Category': i.tag,
                                'Key': c.attrib['key'],
                                'Value': c.attrib['value']})
       return pd.DataFrame(param_ls)


   def parse_initcfg(xml_file):
       root = ET.parse(xml_file).getroot()
       param_ls = []
       for i in root:
           for c in i:
               for k, v in c.attrib.items():
                   param_ls.append({'Category':f"{i.tag}-{c.tag}",
                                    'Key': k,
                                    'Value':v})
       return pd.DataFrame(param_ls)


   def parse_proccfg(xml_file):
       root = ET.parse(xml_file).getroot()
       param_ls = []
       for i in root:
           param_ls.append({'Category':root.tag,
                            'Key':i.attrib['Key'],
                            'Value':i.attrib['Value']})
       return pd.DataFrame(param_ls)


   def parse_execfg(xml_file):
       root = ET.parse(xml_file).getroot()
       param_ls = []
       for i in root[0]:
           param_ls.append({'Category':root.tag,
                            'Key':i.attrib['Process'],
                            'Value':i.attrib['ExeTime']})
       return pd.DataFrame(param_ls)

The If/Else Approach
^^^^^^^^^^^^^^^^^^^^

In order to use the correct function to parse the 'matching' xml file, we could use the if/else statements to check for the xml file name or file content, then use conditional logic to call out the right function to parse the data.

.. code-block:: python

   for cfg_file in glob.glob(os.path.join(cfg_path, "*.xml")):

       cfg_name = os.path.basename(cfg_file)

       if cfg_name == "sysconfig.xml":
           df = parse_syscfg(cfg_file)

       elif cfg_name == "initconfig.xml":
           df = parse_initcfg(cfg_file)

       elif cfg_name == "processconfig.xml":
           df = parse_proccfg(cfg_file)

       elif cfg_name == "execonfig.xml":
           df = parse_execfg(cfg_file)

       else:
           pass

       # continue other processes

The if/else method, although it works, will become cumbersome as more file types are added. One way to mitigate this is to use Caller Dispatch or Dispatch Tables.

The Call Dispatch Approach
^^^^^^^^^^^^^^^^^^^^^^^^^^

Set up a dictionary using the logic 'keys' as dictionary keys and the corresponding function as the values.

.. code-block:: python

   dispatch = {
       'sysconfig.xml': parse_syscfg,
       'initconfig.xml': parse_initcfg,
       'processconfig.xml': parse_proccfg,
       'execonfig.xml': parse_execfg
   }

   for cfg_file in glob_glob(os.path.join(cfg_path, "*.xml")):

       cfg_name = os.path.basename(cfg_file)
       df = dispatch[cfg_name](cfg_file)

       # continue further processes

Using Caller Dispatch enables the flexibility to add and remove functions in the dictionary, and we can easily introduce validation to handle or capture exceptions.

.. code-block:: python

   dispatch = {
       'sysconfig.xml': parse_syscfg,
       'initconfig.xml': parse_initcfg,
       'processconfig.xml': parse_proccfg,
       'execonfig.xml': parse_execfg
   }

   # Loop through all xml files in defined 'cfg_path'
   for cfg_file in glob_glob(os.path.join(cfg_path, "*.xml")):

       cfg_name = os.path.basename(cfg_file)
       try:
           df = dispatch[cfg_name](cfg_file)
       except KeyError as ke:
           # either print or raise the error
           print(f"Configuration not found, expected either {dispatch.keys()}, given {cfg_name}")

       # continue further processes

Conclusion
^^^^^^^^^^

Using Caller Dispatch / Dispatch Tables is way more robust, and the code is lesser, cleaner, and much more readable.
