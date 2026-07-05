import sys
import logging
logging.basicConfig(level=logging.DEBUG)

from magic_pdf.pipe.UNIPipe import UNIPipe
from magic_pdf.rw.DiskReaderWriter import DiskReaderWriter
from pathlib import Path

pdf_path = r"d:\LogManagement\scratch\test.pdf"
try:
    print("Reading PDF...")
    with open(pdf_path, 'rb') as f:
        pdf_bytes = f.read()

    print("Init writers...")
    image_writer = DiskReaderWriter(r"d:\LogManagement\scratch\api_output")
    md_writer = DiskReaderWriter(r"d:\LogManagement\scratch\api_output")
    print("Init pipe...")
    pipe = UNIPipe(pdf_bytes, {"_pdf_type": "", "model_list": []}, image_writer)

    print("Starting pipe_classify...")
    pipe.pipe_classify()
    print("Starting pipe_analyze...")
    pipe.pipe_analyze()
    print("Starting pipe_parse...")
    pipe.pipe_parse()
    print("Starting pipe_mk_markdown...")
    md_content = pipe.pipe_mk_markdown("test_api", drop_mode="none")
    md_writer.write(content=md_content.encode('utf-8'), path="test_api.md")
    print("Done")
except Exception as e:
    import traceback
    traceback.print_exc()
