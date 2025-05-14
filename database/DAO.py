from database.DB_connect import DBConnect
from model.products import Product


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_colori():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct gp.Product_color 
                    from go_sales.go_products gp  """

        cursor.execute(query, ())

        for row in cursor:
            result.append(row["Product_color"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllProducts():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select *
                    from go_sales.go_products gp """

        cursor.execute(query, ())

        for row in cursor:
            result.append(Product(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodesFromColor(color):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select *
                       from go_sales.go_products gp
                       where Product_color = %s """

        cursor.execute(query, (color,))

        for row in cursor:
            result.append(Product(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(anno, colore):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ 
                    select distinct gdsb.Retailer_code ,gdsa.Product_number as P1, gdsb.Product_number as P2, gp1.Product_color, gp2.Product_color ,count(distinct gdsb.`Date`) as weight
                    from go_sales.go_daily_sales gdsa, go_sales.go_daily_sales gdsb, go_sales.go_products gp1, go_sales.go_products gp2
                    where year(gdsa.`Date`)=%s
                    and gdsa.Retailer_code = gdsb.Retailer_code
                    and gdsa.Product_number <> gdsb.Product_number
                    and gdsa.Product_number < gdsb.Product_number
                    and gdsa.`Date` = gdsb.`Date`
                    and gdsa.Product_number = gp1.Product_number
                    and gdsb.Product_number = gp2.Product_number
                    and gp1.Product_color = %s
                    and gp2.Product_color = %s
                    group by gdsa.Product_number , gdsb.Product_number"""

        cursor.execute(query, (anno,colore, colore))

        for row in cursor:
            result.append((row["P1"], row["P2"], row["weight"]))
        cursor.close()
        conn.close()

        return result
