from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import WellnessEntry
from .forms import WellnessEntryForm


@login_required
def add_entry(request):
    today = timezone.now().date()
    existing = WellnessEntry.objects.filter(user=request.user, date=today).first()
    if request.method == 'POST':
        form = WellnessEntryForm(request.POST, instance=existing)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            messages.success(request, 'Saved!')
            return redirect('data:history')
    else:
        form = WellnessEntryForm(instance=existing)
    return render(request, 'data/add_entry.html', {'form': form, 'existing': existing, 'today': today})


@login_required
def history(request):
    entries = WellnessEntry.objects.filter(user=request.user).order_by('-date')
    return render(request, 'data/history.html', {'entries': entries, 'total': entries.count()})


@login_required
def detail(request, pk):
    entry = get_object_or_404(WellnessEntry, pk=pk, user=request.user)
    return render(request, 'data/detail.html', {'entry': entry})


@login_required
def edit(request, pk):
    entry = get_object_or_404(WellnessEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WellnessEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated!')
            return redirect('data:history')
    else:
        form = WellnessEntryForm(instance=entry)
    return render(request, 'data/edit.html', {'form': form, 'entry': entry})


@login_required
def delete(request, pk):
    entry = get_object_or_404(WellnessEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        messages.success(request, 'Deleted!')
        return redirect('data:history')
    return render(request, 'data/confirm_delete.html', {'entry': entry})


@login_required
def stats(request):
    entries = WellnessEntry.objects.filter(user=request.user).order_by('date')
    if not entries.exists():
        messages.info(request, 'No data yet!')
        return redirect('data:add')
    latest = entries.last()
    count = entries.count()
    return render(request, 'data/stats.html', {
        'latest': latest, 'count': count,
        'avg_sleep': round(sum(e.sleep_hours for e in entries)/count, 1),
        'avg_anxiety': round(sum(e.anxiety_level for e in entries)/count, 1),
        'avg_stress': round(sum(e.stress_level for e in entries)/count, 1),
        'avg_mood': round(sum(e.mood_rating for e in entries)/count, 1),
        'entries': entries,
    })