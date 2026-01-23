import pyodbc
from datetime import datetime

# Database connection parameters
SERVER = "mysqlserver"
USERNAME = "abc"
PASSWORD = "pwd"
DATABASE = "master"

def get_connection():
    """
    Establish and return a connection to the SQL Server database.
    
    Returns:
        pyodbc.Connection: Database connection object
        
    Raises:
        Exception: If connection fails
    """
    try:
        connection_string = f"Driver={{ODBC Driver 17 for SQL Server}};Server={SERVER};uid={USERNAME};pwd={PASSWORD};Database={DATABASE}"
        conn = pyodbc.connect(connection_string)
        print("✓ Database connection successful")
        return conn
    except Exception as e:
        print(f"✗ Database connection failed: {str(e)}")
        raise


def create_product(pname, qty, price):
    """
    Insert a new product into the PRODUCTS table.
    
    Args:
        pname (str): Product name
        qty (int): Quantity
        price (float): Product price
        
    Returns:
        int: Product ID of the newly created product, or None if failed
    """
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Insert product and get the generated ID
        query = "INSERT INTO PRODUCTS (pname, qty, price) VALUES (?, ?, ?)"
        cursor.execute(query, (pname, qty, price))
        conn.commit()
        
        # Get the last inserted ID
        cursor.execute("SELECT @@IDENTITY as pid")
        pid = cursor.fetchone()[0]
        
        print(f"✓ Product created successfully with ID: {pid}")
        return int(pid)
        
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"✗ Create product failed: {str(e)}")
        return None
        
    finally:
        if conn:
            conn.close()


def read_product(pid):
    """
    Retrieve a product by ID from the PRODUCTS table.
    
    Args:
        pid (int): Product ID
        
    Returns:
        dict: Product details {pid, pname, qty, price}, or None if not found
    """
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        query = "SELECT pid, pname, qty, price FROM PRODUCTS WHERE pid = ?"
        cursor.execute(query, (pid,))
        row = cursor.fetchone()
        
        if row:
            product = {
                'pid': row[0],
                'pname': row[1],
                'qty': row[2],
                'price': row[3]
            }
            print(f"✓ Product retrieved: {product}")
            return product
        else:
            print(f"✗ Product with ID {pid} not found")
            return None
            
    except Exception as e:
        print(f"✗ Read product failed: {str(e)}")
        return None
        
    finally:
        if conn:
            conn.close()


def read_all_products():
    """
    Retrieve all products from the PRODUCTS table.
    
    Returns:
        list: List of product dictionaries, or empty list if no products
    """
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        query = "SELECT pid, pname, qty, price FROM PRODUCTS"
        cursor.execute(query)
        rows = cursor.fetchall()
        
        products = []
        for row in rows:
            product = {
                'pid': row[0],
                'pname': row[1],
                'qty': row[2],
                'price': row[3]
            }
            products.append(product)
        
        print(f"✓ Retrieved {len(products)} product(s)")
        return products
        
    except Exception as e:
        print(f"✗ Read all products failed: {str(e)}")
        return []
        
    finally:
        if conn:
            conn.close()


def update_product(pid, pname=None, qty=None, price=None):
    """
    Update a product in the PRODUCTS table.
    
    Args:
        pid (int): Product ID (required)
        pname (str, optional): New product name
        qty (int, optional): New quantity
        price (float, optional): New price
        
    Returns:
        bool: True if update successful, False otherwise
    """
    conn = None
    try:
        if not any([pname, qty, price]):
            print("✗ At least one field must be provided for update")
            return False
        
        conn = get_connection()
        cursor = conn.cursor()
        
        # Build dynamic update query
        updates = []
        params = []
        
        if pname is not None:
            updates.append("pname = ?")
            params.append(pname)
        if qty is not None:
            updates.append("qty = ?")
            params.append(qty)
        if price is not None:
            updates.append("price = ?")
            params.append(price)
        
        params.append(pid)  # Add pid at the end for WHERE clause
        
        query = f"UPDATE PRODUCTS SET {', '.join(updates)} WHERE pid = ?"
        cursor.execute(query, params)
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"✓ Product {pid} updated successfully")
            return True
        else:
            print(f"✗ Product with ID {pid} not found")
            return False
            
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"✗ Update product failed: {str(e)}")
        return False
        
    finally:
        if conn:
            conn.close()


def delete_product(pid):
    """
    Delete a product from the PRODUCTS table.
    
    Args:
        pid (int): Product ID
        
    Returns:
        bool: True if deletion successful, False otherwise
    """
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        query = "DELETE FROM PRODUCTS WHERE pid = ?"
        cursor.execute(query, (pid,))
        conn.commit()
        
        if cursor.rowcount > 0:
            print(f"✓ Product {pid} deleted successfully")
            return True
        else:
            print(f"✗ Product with ID {pid} not found")
            return False
            
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"✗ Delete product failed: {str(e)}")
        return False
        
    finally:
        if conn:
            conn.close()


# Example usage
if __name__ == "__main__":
    print("=== PRODUCTS CRUD Operations ===\n")
    
    # Create products
    print("1. Creating products...")
    pid1 = create_product("Laptop", 10, 999.99)
    pid2 = create_product("Mouse", 50, 29.99)
    
    print("\n2. Reading all products...")
    products = read_all_products()
    for product in products:
        print(f"  {product}")
    
    print("\n3. Reading specific product...")
    if pid1:
        product = read_product(pid1)
    
    print("\n4. Updating product...")
    if pid1:
        update_product(pid1, qty=15, price=1099.99)
    
    print("\n5. Reading updated product...")
    if pid1:
        product = read_product(pid1)
    
    print("\n6. Deleting product...")
    if pid2:
        delete_product(pid2)
    
    print("\n7. Final product list...")
    products = read_all_products()
    for product in products:
        print(f"  {product}")
