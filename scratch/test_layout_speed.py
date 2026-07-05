import os
import sys
import time
import logging

logging.basicConfig(level=logging.INFO)
# Don't restrict threads completely, just use defaults to see if it's faster
# os.environ["OMP_NUM_THREADS"] = "4"

from magic_pdf.model.doc_analyze_by_custom_model import ModelSingleton
from magic_pdf.libs.config_reader import get_device

def test_layout():
    device = get_device()
    print(f"Using device: {device}")
    start = time.time()
    model_manager = ModelSingleton()
    model = model_manager.get_model(
        ocr=False,
        show_log=True,
        lang=None,
        layout_model=None,
        formula_enable=False,
        table_enable=False
    )
    print(f"Model initialized in {time.time()-start:.2f}s")
    
    import fitz
    import numpy as np
    
    pdf_path = r"d:\LogManagement\scratch\test.pdf"
    doc = fitz.open(pdf_path)
    page = doc[0]
    pix = page.get_pixmap(dpi=150)
    img_data = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    if pix.n == 4:
        import cv2
        img_data = cv2.cvtColor(img_data, cv2.COLOR_RGBA2RGB)
    
    print(f"Extracted image {img_data.shape}. Running layout prediction...")
    pred_start = time.time()
    res = model.layout_model.batch_predict([img_data], 1)
    print(f"Layout predicted in {time.time()-pred_start:.2f}s")
    print("Result items:", len(res[0]))

if __name__ == '__main__':
    test_layout()
