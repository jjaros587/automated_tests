from utils import utilsMain

utilsMain.delete_assets_folder()
result = utilsMain.parse_args()
utilsMain.verify_args(result['parse'], result['args'])
utilsMain.run_tests()
utilsMain.zip_screenshots()