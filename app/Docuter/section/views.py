from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Section, Question, Option
from .forms import QuestionForm, OptionForm

# ... PDF and Word generation functions (explained later)


def create_question(request):
    if request.method == "POST":
        # Handle question and option creation (forms for adding options)
        pass
    else:
        question_form = QuestionForm()
        option_form = OptionForm()
        return render(
            request,
            "create_question.html",
            {"question_form": question_form, "option_form": option_form},
        )


def generate_document(request):
    sections = Section.objects.all()
    # ... Logic to retrieve questions, options, and format data

    # PDF Generation
    pdf = FPDF()
    # ... Add content from sections to PDF
    pdf.output("my_document.pdf")

    # Word Document Generation
    doc = docx.Document()
    # ... Add content from sections to Word document
    doc.save("my_document.docx")

    # Assuming you just want to trigger download in browser:
    response = HttpResponse(
        pdf.output(dest="S").encode("latin-1"), content_type="application/pdf"
    )  # For PDF
    response["Content-Disposition"] = "attachment; filename=my_document.pdf"
    return response
