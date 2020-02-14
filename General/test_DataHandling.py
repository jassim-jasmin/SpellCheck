from unittest import TestCase
from General.DataHandling import DataHandling
from General.FileDataProcessing import DirectoryHandling


class TestDataHandling(TestCase):
    def setUp(self) -> None:
        self.dataHandlingObj = DataHandling()

    def tearDown(self) -> None:
        del self.dataHandlingObj

    def test_csv_to_df(self):
        data = self.dataHandlingObj.csvToDF('../Test/name_test_1.txt', ',', self.dataHandlingObj.inputNameSetHeader)
        self.assertNotEqual(True, data.empty, 'Text file data frame conversion error')
        # print(data)

    def test_merge_data_frame(self):
        df = self.dataHandlingObj.csvToDF('../Test/name_test_1.txt', ',', self.dataHandlingObj.inputNameSetHeader)
        merge = self.dataHandlingObj.mergeDataFrame(df, '../Test/name_test_2.txt', ',',
                                                    self.dataHandlingObj.inputNameSetHeader)
        self.assertEqual(4, merge.shape[0])
        merge = self.dataHandlingObj.mergeDataFrame(df, '../Test/name_test_2.txt', ',',
                                                    self.dataHandlingObj.inputNameSetHeader, ['name'])
        self.assertEqual(2, merge.shape[0], 'dataframe duplicates are not removed')
        # print(merge)

    def test_make_name_group_dict(self):
        directoryHandlingObj = DirectoryHandling()
        self.dataHandlingObj.makeNameGroupDict(directoryHandlingObj, '../Test/test_dir')
        pass

    def test_make_uniq_name_set(self):
        directoryHandlingObj = DirectoryHandling()
        df = self.dataHandlingObj.makeUniqNameSet(directoryHandlingObj, '../Test/test_dir')

        self.assertEqual(3, df.shape[0], 'MERGING ALL NAME ERRROR')

    def test_save_data_frame_to_json(self):
        directoryHandlingObj = DirectoryHandling()
        df = self.dataHandlingObj.makeUniqNameSet(directoryHandlingObj, '../Test/test_dir')
        self.assertTrue(self.dataHandlingObj.saveDataFrameToJson(df, '../Test/name_set.csv'),
                        'name set saving as csv error')

    def test_read_csv_to_df(self):
        directoryHandlingObj = DirectoryHandling()
        df = self.dataHandlingObj.makeUniqNameSet(directoryHandlingObj, '../Test/test_dir')
        if not df.empty:
            self.assertTrue(self.dataHandlingObj.saveDataFrameToJson(df, '../Test/name_set.csv'), 'saved csv read error')
            dfName = self.dataHandlingObj.readCsvToDF('../Test/name_set.csv')
            self.assertFalse(dfName.empty, 'read name set csv error')
        else:
            self.fail('csv read error')