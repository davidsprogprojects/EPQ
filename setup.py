import cx_Freeze

executables = [cx_Freeze.Executable("The Fear Initiative.py")]

cx_Freeze.setup(name="The Fear Initiative First Draft",
                options={"build_exe": {"packages":["pygame"],
                                       "include_files":["God\God_1.png","God\God_2.png","Map\wall.png","Script\Help.txt","Character\Asleep_1.png","Character\Asleep_2.png","Character\Asleep_3.png","Character\Asleep_4.png","Character\Asleep_5.png","Character\Asleep_6.png","Character\Asleep_7.png","Character\Asleep_8.png","Character\Asleep_9.png","Character\Main_Char_2.png","Character\Main_Char_4.png","Character\Main_Char_3.png","Character\Main_Char_1.png","Devil\Devil_1.png","Devil\Devil_2.png","Map\Tutorial1.png","Devil1.txt","God1.txt","Map\Tutorial2.png","Map\Tutorial3.png","Map\Tutorial3_1.png","Map\Tutorial4.png","Map\Tutorial4_1.png","Map\Tutorial4_2.png","Map\Map1.png","Map\Map2.png","Map\Map3.png","Map\Map4.png","Map\Map4_1.png","Map\Puzzle1.png","Map\Puzzle1_Level2+.png","Map\Puzzle1_1.png","Map\Puzzle1_Level2+_1.png"]}},
                executables = executables

                )
