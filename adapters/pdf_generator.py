import reportlab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from PIL import Image as PILImage

class BookPDFGenerator:
    def __init__(self, output_path='book.pdf'):
        """
        Initialize the PDF generator with custom styles
        
        :param output_path: Path where the PDF will be saved
        """
        self.output_path = output_path
        
        # Create custom styles directly instead of modifying existing ones
        self.styles = {
            'CustomTitle': ParagraphStyle(
                'CustomTitle',
                parent=getSampleStyleSheet()['Normal'],
                fontSize=24,
                textColor='black',
                alignment=TA_CENTER,
                spaceAfter=12
            ),
            'CustomSubtitle': ParagraphStyle(
                'CustomSubtitle',
                parent=getSampleStyleSheet()['Normal'],
                fontSize=16,
                textColor='darkblue',
                alignment=TA_LEFT,
                spaceAfter=12
            ),
            'CustomBody': ParagraphStyle(
                'CustomBody',
                parent=getSampleStyleSheet()['Normal'],
                fontSize=10,
                leading=14,
                alignment=TA_LEFT
            )
        }

    def create_book(self, title, summary,text, image_path=""):
        """
        Create a PDF book with given content
        
        :param title: Title of the book
        :param summary: Brief summary
        :param image_path: Path to the cover image
        :param text: Main text content
        """
        # Create the PDF document
        doc = SimpleDocTemplate(
            self.output_path, 
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18
        )
        
        # Story (content) to be added to the PDF
        story = []

        if image_path!="":
            try:
                # Open and resize image
                img = PILImage.open(image_path)
                max_width = 400  # Maximum width
                width_ratio = max_width / img.width
                img_width = max_width
                img_height = int(img.height * width_ratio)
                
                # Add image to story
                story.append(Image(image_path, width=img_width, height=img_height))
                story.append(Spacer(1, 12))
            except Exception as e:
                print(f"Warning: Could not process image - {e}")
        
        # Add title
        story.append(Paragraph(title, self.styles['CustomTitle']))
        story.append(Spacer(1, 12))
        
        # Add summary
        story.append(Paragraph("Summary", self.styles['CustomSubtitle']))
        story.append(Paragraph(summary, self.styles['CustomBody']))
        story.append(Spacer(1, 12))
        
        # # Add cover image if exists and is valid
       
        
        # Add main text
        story.append(Paragraph("Content", self.styles['CustomSubtitle']))
        
        # Split text into paragraphs and add
        paragraphs = text.split('\n\n')
        for paragraph in paragraphs:
            story.append(Paragraph(paragraph, self.styles['CustomBody']))
            story.append(Spacer(1, 6))
        
        # Build PDF
        doc.build(story)
        
        print(f"PDF created successfully at {self.output_path}")
        return self.output_path