===================
About the test data
===================

要抓資料的對象是中央氣象局的 `即時海況`_ .
測資為 ``data.json``.

實際抓資料後發現它的 HTML 設計不良.
為了不浪費時間, 所以先手動生出 JSON 測資.
若用 BeautifulSoup 之類的 parser 解開後仍需要一點程式重新整理其 data.

另外, 請教專業的衝浪教練後得知, `即時海況`_ 資訊對衝浪而言遠遠不足.
衝浪需要更多外海與颱風動態等資訊, 僅僅是近海的海潮資訊不夠.
相關資訊服務已有人提供. 參考資料待補.

.. _即時海況: http://www.cwb.gov.tw/V7/marine/sea_condition/cht/allData.html
